import './App.css';
import { useState } from "react";
import DisplayTable from './Tables';

function App() {
  // Variables for maintaining state
  const [entry_id, setEntryId] = useState("");
  const [assembly_id, setAssemblyId] = useState("");
  const [interface_id, setInterfaceId] = useState("");
  const [roundValue, setRoundValue] = useState(false);
  const [roundingValue, setRoundingValue] = useState(2);
  const [buttonValue, setButtonValue] = useState("Calculate");
  const [active, setActive] = useState(false);
  const [data, setData] = useState([]);
 
  // Function called when calculate button is clicked
  let handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await fetch("http://127.0.0.1:8000/asa-change", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          "entry_id": entry_id,
          "assembly_id": assembly_id,
          "interface_id": interface_id,
        }),
      }).then(response => response.json())
      .then(response => {
        // console.log(response);
        setData(response);
        if(active)
          setActive(!active);
        setButtonValue("Calculate");
      });

    } catch (err) {
      console.log(err);
      alert("No Data Found. Try different parameters");
    }
  };

  // Function for rounding toggle button 
  let handleChange = () => {
    // console.log(JSON.stringify({
    //   "roundValue": roundValue,
    //   "roundingValue": roundingValue
    // }));

    try{
      fetch("http://127.0.0.1:8000/is-rounded", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          "roundValue": roundValue,
          "roundingValue": roundingValue
        }),
      }).then(response => response.json())
      .then(response => {
        // console.log("Toggler: ", response);
      });
    } catch(err){
      console.log(err);
    }
  }

  return (
    <div class="container-fluid mt-2">
      <form class="form-inline" onSubmit={handleSubmit}>
      <label for="entry_id">Entry ID:</label>
      <input 
        type="text" 
        id="entry_id" 
        placeholder="Enter Entry id" 
        name="entry_id"
        value={entry_id}
        required
        onChange={(e) => setEntryId(e.target.value)}
      />
      <label for="assembly_id">Assembly ID:</label>
      <input 
        type="text" 
        id="assembly_id" 
        placeholder="Enter Assembly id" 
        name="assembly_id"
        value={assembly_id}
        required
        onChange={(e) => setAssemblyId(e.target.value)}
      />
      <label for="interface_id">Interface ID:</label>
      <input 
        type="text" 
        id="interface_id" 
        placeholder="Enter Interface id" 
        name="interface_id"
        value={interface_id}
        required
        onChange={(e) => setInterfaceId(e.target.value)}
      />
      <button type="submit" style={{ backgroundColor: active ? "green" : "royalblue" }}>{buttonValue}</button>
    </form>
    <div className='form-inline'>
      <div class="custom-control custom-switch align-self-stretch">
          <input type="checkbox" class="custom-control-input" id="customSwitches" onChange={(e) => {setRoundValue(!roundValue); if(!active) setActive(!active); setButtonValue("Recalculate"); }}/>
          <label class="custom-control-label" for="customSwitches">Toggle for Round values</label>
      </div>
      {roundValue && (<input 
        type="number" 
        id="rounding_value" 
        placeholder="Rounding Value" 
        name="rounding_value"
        value={roundingValue}
        onChange={(e) => {
          // Handling negative values using regex
          if (/^[0-9]*$/.test(e.target.value)) {
            setRoundingValue(e.target.value);
          }
          if(!active)
            setActive(!active);
          setButtonValue("Recalculate");
        }}
      />)}

      {handleChange()}
        
    </div>

    {data && data.map((item) => {
      // console.log(item.interface_partner_feature["asym_id"]);
      return (<DisplayTable heading={item.interface_partner_feature} data={item.table_data}/>)
    })}
    </div>
  );
}

export default App;
