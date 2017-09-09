import json
import os
import sqlite3

import requests


class StoragePool():

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def add_key(self, key, pwd):
        self.data[key] = pwd

    def get_key(self, key):
        return self.data.get(key)


class JsonStoragePool(StoragePool):

    def __init__(self, path):

        self.path = path
        if os.stat(path).st_size != 0:
            with open(path) as file:
                self.json_data = json.load(file)
                super(JsonStoragePool, self).__init__(self.json_data)
        else:
            raise IOError("StoragePool file is empty.")

    def add_key(self, key, pwd):
        super().add_key(key, pwd)
        new_data = self.get_data()
        with open(self.path, 'w') as file:
            file.write(json.dumps(new_data))

class SqLiteStoragePool(StoragePool):

    def __init__(self, path):
        self.path = path
        with sqlite3.connect(path) as conn:
            if os.path.isfile(path):
                with conn:
                    try:
                        data = conn.execute("SELECT * FROM keys").fetchall()
                        self.data = dict(data)
                    except sqlite3.Error as e:
                        print("An error occurred:", e.args[0])
            else:
                raise sqlite3.Error("No database")
            super(SqLiteStoragePool, self).__init__(self.data)

    def add_key(self, key, pwd):
        new_data = (key, pwd)
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()
            try:
                c.execute('INSERT INTO keys VALUES (?,?)', new_data)
                conn.commit()
            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])

    def get_key(self, url):
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()
            try:
                key = c.execute('SELECT password FROM keys WHERE url = ?', (url,)).fetchone()
                if key:
                    return key[0]
            except sqlite3.Error as e:
                print("An error occurred:", e.args[0])


class RequestModule():

    def __init__(self, storage):
        self.storage = storage

    def send_request(self, url):
        token = self.storage.get_key(url)
        headers = {'Token': token}
        r = requests.get(url, headers=headers)
        return self.proc_response(r)

    def proc_response(self, response):
        print(json.dumps(response.text))
        return response

def main():
    storage_path = './storage.json'
    storage_path2 = './storage.db'
    storage = JsonStoragePool(storage_path)
    storage2 = SqLiteStoragePool(storage_path2)

    module = RequestModule(storage)
    module.send_request('http://google.com')


if __name__ == '__main__':
    main()


