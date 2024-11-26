import numpy as np
from Bio.Data import IUPACData

def iupac_match_score(a, b, match_score=1, mismatch_score=-1):
    if a == b:
        return match_score
    # Check if either character is an IUPAC code
    if a in IUPACData.ambiguous_dna_values:
        if b in IUPACData.ambiguous_dna_values[a]:
            return match_score
    if b in IUPACData.ambiguous_dna_values:
        if a in IUPACData.ambiguous_dna_values[b]:
            return match_score
    return mismatch_score


def smith_waterman_iupac(seq1, seq2, gap_penalty=-2):
    m, n = len(seq1), len(seq2)
    score_matrix = np.zeros((m + 1, n + 1), dtype=float)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score_matrix[i - 1][j - 1] + iupac_match_score(seq1[i - 1], seq2[j - 1])
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(0, int(match), int(delete), int(insert))

    return score_matrix


def traceback_iupac(score_matrix, seq1, seq2, gap_penalty=-2):
    i, j = np.unravel_index(np.argmax(score_matrix), score_matrix.shape)
    align1, align2, match_line = '', '', ''
    end_index = i
    start_index = i

    while score_matrix[i][j] > 0:
        score = score_matrix[i][j]
        diag = score_matrix[i - 1][j - 1]
        up = score_matrix[i][j - 1]
        left = score_matrix[i - 1][j]

        if score == diag + iupac_match_score(seq1[i - 1], seq2[j - 1]):
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            # Use '|' for exact matches and valid IUPAC matches; use 'X' for mismatches
            match_line = ('|' if (seq1[i - 1] == seq2[j - 1] or
                                  (seq2[j - 1] in IUPACData.ambiguous_dna_values and
                                   seq1[i - 1] in IUPACData.ambiguous_dna_values[seq2[j - 1]]))
                          else 'X') + match_line
            i -= 1
            j -= 1
        elif score == left + gap_penalty:
            align1 = seq1[i - 1] + align1
            align2 = '-' + align2
            match_line = ' ' + match_line
            i -= 1
        elif score == up + gap_penalty:
            align1 = '-' + align1
            align2 = seq2[j - 1] + align2
            match_line = ' ' + match_line
            j -= 1

        start_index = i + 1

    # Handle unmatched parts of seq2 at the beginning and end
    if j > 0:
        align1 = '-' * j + align1
        align2 = seq2[:j] + align2
        match_line = 'X' * j + match_line

    if len(align2) < len(seq2):
        remaining = len(seq2) - len(align2)
        align1 += '-' * remaining
        align2 += seq2[-remaining:]
        match_line += 'X' * remaining

    return align1, align2, match_line, start_index, end_index

def smith_waterman_alignment_iupac(seq1, seq2):
    score_matrix = smith_waterman_iupac(seq1, seq2)
    align1, align2, match_line, start_index, end_index = traceback_iupac(score_matrix, seq1, seq2)
    return align1, align2, match_line, np.int64(start_index), np.int64(end_index), np.int64(np.max(score_matrix))