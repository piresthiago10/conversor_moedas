<template>
  <body>
    <div class="title">Conversor de Correção Monetária</div>
    <div class="container">
      <form @submit.prevent="salvar" class="form-inline">
        <label for="fname">De:</label><br />
        <select id="moeda_origem" name="moeda_origem" v-model="conversao.from">
          <option value="USD" selected>USD</option>
          <option value="BRL">BRL</option>
          <option value="EUR">EUR</option>
          <option value="BTC">BTC</option>
          <option value="ETH">ETH</option>
        </select>
        <input
          type="number"
          step="0.01"
          min="0"
          id="valor_conversao"
          name="valor_conversao"
          v-model="conversao.amount"
        /><br />
        <label for="fname">Para:</label><br />
        <select id="moeda_final" name="moeda_final" v-model="conversao.to">
          <option value="USD">USD</option>
          <option value="BRL" selected>BRL</option>
          <option value="EUR">EUR</option>
          <option value="BTC">BTC</option>
          <option value="ETH">ETH</option>
        </select>
        <button type="submit">Converter</button>
      </form>
    </div>

    <div class="sub-title">Histórico de conversão:</div>

    <div class="table">
      <table id="last-convertions">
        <tr>
          <th>ID</th>
          <th>Moeda de origem</th>
          <th>Valor a ser convertido</th>
          <th>Moeda final</th>
          <th>Valor convertido</th>
          <th>Data e hora</th>
        </tr>
        <tr v-for="item of listagem" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.moeda_origem }}</td>
          <td>{{ item.valor_conversao }}</td>
          <td>{{ item.moeda_final }}</td>
          <td>{{ item.valor_convertido }}</td>
          <td>{{ item.data_hora }}</td>
        </tr>
      </table>
    </div>
  </body>
</template>

<script>
import Listagem from "./services/conversao";

export default {
  data() {
    return {
      conversao: {
        from: "",
        to: "",
        amount: "",
      },

      listagem: [],
    };
  },

  mounted() {
    this.listar()
  },

  methods: {
    listar() {
      Listagem.listar().then((response) => {
        this.listagem = response.data;
      });
    },

    salvar() {
      Listagem.salvarConsulta(this.conversao).then(() => {
        this.conversao = {}
        this.listar()
      });
    },
  },
};
</script>

<style>
body {
  font-family: "Roboto", sans-serif;
  margin: 0px;
}

p {
  color: blue;
}

.container {
  width: 100vw;
  height: 15vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.title {
  background-color: #cfcdb4;
  font-size: 70px;
  color: #1f3447;
  font-weight: bold;
  width: 100vw;
  height: 20vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.sub-title {
  font-size: 35px;
  color: #1f3447;
  font-weight: bold;
  width: 90vw;
  height: 5vh;
  display: flex;
  flex-direction: row;
  justify-content: start;
  padding: 1em;
}

.table {
  width: 95vw;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0.5em;
}

.form-inline {
  display: flex;
  flex-flow: row wrap;
  align-items: center;
}

.form-inline label {
  margin: 5px 10px 5px 0;
  padding: 10px;
}

.form-inline input {
  vertical-align: middle;
  margin: 5px 10px 5px 10px;
  padding: 10px;
  background-color: #fff;
  border: 1px solid #ddd;
}

.form-inline button {
  padding: 10px 20px;
  width: 100px;
  background-color: #6d8ead;
  border: 1px solid #ddd;
  color: white;
  cursor: pointer;
  margin-left: 10px;
}

.form-inline button:hover {
  background-color: #1f3447;
}

.form-inline select {
  background-color: #6d8ead;
  padding: 8px 20px;
  color: white;
  width: 100px;
}

#last-convertions {
  border-collapse: collapse;
  width: 90%;
}

#last-convertions td,
#last-convertions th {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

#last-convertions tr:nth-child(even) {
  background-color: #f2f2f2;
}

#last-convertions tr:hover {
  background-color: #ddd;
}

#last-convertions th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: center;
  background-color: #6d8ead;
  color: white;
}
</style>
