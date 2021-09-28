import  { http } from './config'

export default {
    listar:()=>{
        return http.get('listagem')
    },

    salvarConsulta:(conversao)=>{
        return http.get(`conversao/?from=${conversao.from}&to=${conversao.to}&amount=${conversao.amount}`)
    }
}
  