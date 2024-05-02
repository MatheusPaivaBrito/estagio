import React, {useEffect, useState} from 'react';
import { IonItem, IonLabel, IonList } from '@ionic/react';
import DataTable, { TableColumn } from 'react-data-table-component';
import axios from 'axios';
import { idCard } from 'ionicons/icons';

const Tab1: React.FC = () => {

  const [data, setdata] = useState([])

  const visualizar = () => {
    axios({
      method: 'get',
      url: 'http://localhost:8000/',
    }).then(function (response) {
      setdata(response.data);
    });
  }
  useEffect(() => {
    visualizar();
  }, []);

  const columns: TableColumn<{ id: number; nome: string; email: number; city: string; }>[] = [
    {
      name: 'ID',
      selector: (row) => row.id,
      sortable: true
    },
    {
      name: 'Nome',
      selector: (row) => row.nome,
      sortable: true
    },
    {
      name: 'email',
      selector: (row) => row.email,
      sortable: true
    }
  ];

  return (
      <DataTable
        title="Dados dos Usuários"
        columns={columns}
        data={data}
        pagination
        selectableRows
      />
  );
};

export default Tab1;
