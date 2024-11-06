from backend.src.database.mongodb.genomic_upload_test import collection
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType
from backend.src.pathogens.pathogen import Pathogen

if __name__ == '__main__':
    mongodb_connector = MongoDBConnector(force_ssl=True)
    mongodb_connector.ping()

    pathogen = Pathogen(taxonomy_id='taxonomy_id', scientific_name='scientific_name', source_db='source_db',
                        genomic_sequence='genomic_sequence')

    # mongodb_connector.upload_document(pathogen.to_document(), CollectionType.PATHOGENS)

    # mongodb_connector.fetch_document({}, CollectionType.PATHOGENS)
