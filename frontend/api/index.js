import axios from 'axios';


export default {
    fetchCartas(method, params, data){
        if(method === 'post'){
            return ajax('cp/api/letters/', method, { data });
        }else{
            return ajax('cp/api/letters/', method, {});
        }
    }
}

/*
*@param url
*@param method
*@param params
*@param data
*@returns
*/

function ajax(url, method, options) {
    if(options !== undefined){
        var {params ={}, data = {}} = options
    }else{
        params = data = {}
    }
    return new Promise(( resolve, reject ) => {
        axios({
            url,
            method,
            params,
            data
        }).then(res => {
            resolve(res)
        }, res => {
            reject(res)
        })
    })
}