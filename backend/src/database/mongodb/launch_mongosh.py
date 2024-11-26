import subprocess
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector

"""
Launches a mongosh session using the connection URI from MongoDBConnector.
mongosh is installed on macos with brew:
brew tap mongodb/brew
brew install mongosh
"""


def main():
    # Instantiate the connector and get the URI
    connector = MongoDBConnector()
    uri = connector.get_connection_uri()

    #   Print the URI for verification
    

    # Run the mongosh command with the URI
    try:
        command = f'mongosh "{uri}"'
        subprocess.run(command, shell=True)
    except Exception as e:
        print("Failed to launch mongosh:", e)


if __name__ == "__main__":
    main()
