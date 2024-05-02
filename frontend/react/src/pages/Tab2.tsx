import React, {useState} from 'react';
import { IonInput, IonItem, IonList, IonButton } from '@ionic/react';
import axios from 'axios';

const Tab2: React.FC = () => {
  const [nome, setnome] = useState("")
  const [email, setemail] = useState("")

  const salvar = () => {
    axios({
      method: 'post',
      url: 'http://localhost:8000/add/',
      data: {
        name: nome,
        email: email
      }
    });    
  }
  return (
    <IonList>
      <IonItem>
        <IonInput label="Nome" onIonInput={(e: any) => setnome(e.target.value)}></IonInput>
      </IonItem>
      <IonItem>
        <IonInput label="email" onIonInput={(e: any) => setemail(e.target.value)}></IonInput>
      </IonItem>
      <IonItem>
        <IonButton slot="end" color="success" onClick={salvar}>Salvar</IonButton>
      </IonItem>
    </IonList>
  );
};

export default Tab2;
