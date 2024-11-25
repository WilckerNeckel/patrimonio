
import React, { useState } from 'react';
import './App.css';
import { listagemEquipamentos, entradaSaida } from './api/api';

function App() {
  const [rfidPessoa, setRfidPessoa] = useState('');
  const [rfidPatrimonio, setRfidPatrimonio] = useState('');
  const [rfidSetor, setRfidSetor] = useState('');
  const [equipamentos, setEquipamentos] = useState([]);
  const [rfidSetorInput, setRfidSetorInput] = useState('');

  const handleEntradaSaida = async () => {
    const response = await entradaSaida(rfidPessoa, rfidPatrimonio, rfidSetorInput);
    console.log(response)
    if (response.funcionario) {
      if (response.movimentacao == "entrada"){
        alert('Entrada realizada com sucesso!');
      }
      if (response.movimentacao == "saida"){
        alert('Saida realizada com sucesso')
      };
    } else {
      alert('Movimentação cancelada: crachá do funcionário não encontrado!');
    }
  };

  const handleListagem = async () => {
    const equipamentosJson = await listagemEquipamentos(rfidSetor);
    const equipamentos = equipamentosJson.map((equipamento) => equipamento.descricao + ' - ' + equipamento.rfid_tag);
    console.log(equipamentosJson);
    console.log(equipamentos);
    setEquipamentos(equipamentos);
};

  return (
    <div className="App">
      <div className="secaoEntradaSaida">
        <h1 className="tituloEntradaSaida">Simulação Leitor RFID</h1>
        <div className="camposEntrada">
          <label htmlFor="rfidPessoa">TAG do Funcionario:</label>
          <input
            type="text"
            id="rfidPessoa"
            value={rfidPessoa}
            onChange={(e) => setRfidPessoa(e.target.value)}
            placeholder="Insira a TAG do Funcionario"
          />
          <label htmlFor="rfidPatrimonio">TAG do Patrimônio:</label>
          <input
            type="text"
            id="rfidPatrimonio"
            value={rfidPatrimonio}
            onChange={(e) => setRfidPatrimonio(e.target.value)}
            placeholder="Insira a TAG do patrimônio"
          />
          <label htmlFor="rfidSetorInput">TAG do Setor:</label>
          <input
            type="text"
            id="rfidSetorInput"
            value={rfidSetorInput}
            onChange={(e) => setRfidSetorInput(e.target.value)}
            placeholder="Insira a TAG do patrimônio"
          />
        </div>
        <button className="botaoEntradaSaida" onClick={handleEntradaSaida}>
          Simular Entrada/Saída
        </button>
      </div>

      <div className="secaoListagemEquipamentos">
        <h1 className="tituloListagemEquipamentos">Listagem de Equipamentos por Setor</h1>
        <div className="campoRfidSetor">
          <label htmlFor="rfidSetor">TAG do Setor:</label>
          <input
            type="text"
            id="rfidSetor"
            value={rfidSetor}
            onChange={(e) => setRfidSetor(e.target.value)}
            placeholder="Insira a TAG do setor"
          />
        </div>
        <button className="botaoListagemEquipamentos" onClick={handleListagem}>
          Listar Equipamentos
        </button>
        <ul className="listaEquipamentos">
          {equipamentos.map((equipamento, index) => (
            <li key={index}>{equipamento}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;