from flask import Blueprint, request

from backend.definitions import API_VERSION
from backend.src.smith_wn.smith_wn_service import smith_wn_alignment

bp = Blueprint('smith_wn_controller', __name__)

@bp.route(f'/{API_VERSION}/smith_wn', methods=['POST'])
def run_smith_wn():
    return smith_wn_alignment(request)

