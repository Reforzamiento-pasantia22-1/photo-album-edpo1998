class FetchData{  

    constructor(){
        this._root =  process.env.VITE_BACKEND_ADDR;
    }

    request(url, method, data){
        return new Promise((resolve, reject) => {
            let options = {
                method: method,
                headers: {
                    'Content-Type': 'application/json'
                }
            };

            if(data){
                options.body = JSON.stringify(data);
            }

            fetch(this._root + url, options)
                .then(response => {
                    if(response.ok){
                        return response.json();
                    }
                    else{
                        throw new Error('Error: ' + response.status);
                    }
                })
                .then(data => {
                    resolve(data);
                })
                .catch(error => {
                    reject(error);
                });
        });
    }
}

const fetchdataInstance = new FetchData();

Object.freeze(fetchdataInstance);

export default fetchdataInstance;