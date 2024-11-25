export const listagemEquipamentos = async (rfidSetor) => {
  const response = await fetch(`http://localhost:8000/api/patrimonio?rfidSetor=${rfidSetor}`);
  const equipamentos = await response.json();
  return equipamentos;
}

export const entradaSaida = async (rfidFuncionario, rfidPatrimonio, rfidSetor) => {
  const response = await fetch('http://localhost:8000/api/registro/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      rfidFuncionario,
      rfidPatrimonio,
      rfidSetor
    })
  });
  const movimentacao = await response.json();
  return movimentacao;
}

