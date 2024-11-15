from mongoengine import Document, StringField

from backend.src.helper.collection_type import CollectionType


# TODO: completely different way of pinging MongoDB, will need to discuss with team
# EX: document = Pathogen.objects.get(accession_id=accession_id)


class Pathogen(Document):
    """
    Required / optional fields will need to be determined by the method of retrieval from NCBI.
    Only accession_id marked required for now. Length will also need to be determined later.
    """

    taxonomic_id = StringField(required=False, max_length=100)
    common_name = StringField(required=False, max_length=100)
    gcf_id = StringField(required=False, max_length=100)
    subtype_name = StringField(required=False, max_length=100)
    accession_id = StringField(required=True, max_length=100)
    genomic_sequence = StringField(required=False, max_length=100)
    location = StringField(required=False, max_length=100)
    strain_name = StringField(required=False, max_length=100)
    collection_date = StringField(required=False, max_length=100)
    release_date = StringField(required=False, max_length=100)
    query_date = StringField(required=False, max_length=100)

    meta = {'collection': CollectionType.PATHOGENS}
