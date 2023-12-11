// no
function findOrCreate(jsonObject, key,value) {
    if (jsonObject.hasOwnProperty(key)) {
        jsonObject[key] = value;
        return jsonObject;
    } else {
        let newObj = jsonObject;
        newObj[key] = value; 
        return newObj;
    }
}


class setStorage {
    /**
     * 初始化，當沒有設定過的話就把value給帶進去做初始化，如果有的
     * initialize,do nothing if local storage has been set. 
     * @param {string} key 鍵
     * @param {any} value 值
     */
    constructor(key,value) {

        this.key = key;
        if (localStorage.getItem(this.key)) {}
        else {this.set(value)}
    }

    get() {
        return localStorage.getItem(this.key);
    }

    remove() {
        return localStorage.removeItem(this.key);
    }

    set(value) {
        if (typeof value === 'object') {
            value = JSON.stringify(value);
        }
        localStorage.setItem(this.key,value);
    }

    // no
    update(key,value) {
        let newObj = this.get()
        newObj[key] = value;
        this.set(newObj);
    }
}