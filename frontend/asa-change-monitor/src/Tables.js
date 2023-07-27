import { MDBDataTable } from 'mdbreact';

// Created seperate component so that we can reuse it for any purpose
// Used to display the tables dynamically using the data passed through props

// Additionally I added the search feature in the tables, pagination and responsive layouts for all screens and devices
function DisplayTable(props) {

    const data = {
        columns: [
          {
            label: 'Sr No',
            field: 'srno',
            sort: 'asc'
          },
          {
            label: 'Unbound ASA',
            field: 'unboundasa',
            sort: 'asc'
          },
          {
            label: 'Bound ASA',
            field: 'boundasa',
            sort: 'asc'
          },
          {
            label: 'Change in ASA',
            field: 'changeasa',
            sort: 'asc'
          }
        ],
        rows: props.data
    }

  return (
    <>
      <hr/>
      <h4>Showing Data For: {props.heading["entity_id"]}{props.heading["asym_id"]}</h4>  
      <MDBDataTable striped bordered small responsive data={data}/>
    </>
  );
}

export default DisplayTable;
