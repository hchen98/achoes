import React from "react";
import { Graph } from "react-d3-graph";
import Sidebar from "react-sidebar";

function click() {
  window.alert("This is a click");
}


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      sidebarOpen: false,
      test_input: "",
    };
    this.onSetSidebarOpen = this.onSetSidebarOpen.bind(this);
    this.onClickNode = this.onClickNode.bind(this);
    this.inputHandler = this.inputHandler.bind(this);
  }

  onSetSidebarOpen(open) {
    this.setState({ sidebarOpen: open });
  }

  data = {
    "nodes": [{ "id": "Variable_1" }, { "id": "Variable_2" }, { "id": "Variable_3" }],
    "links": [{ "source": "Variable_1", "target": "Variable_2", "label": "transform" },
    { "source": "Variable_2", "target": "Variable_3", "label": "encoding" },
    ],
  };

  myConfig = {
    "nodeHighlightBehavior": true,
    "height": 600,
    "width": 1200,
    "directed": true,
    "node": {
      "color": "lightgreen",
      "size": 120,
      "highlightStrokeColor": "blue",
    },
    "link": {
      "highlightColor": "lightblue",
      "renderLabel": true,
    },
  };

  onClickNode(nodeId) {
    // this.setState({ isVisible: !this.state.isVisible })
    var return_data = { type: "node", val: nodeId };
    this.onSetSidebarOpen(true);
    // window.alert(`Clicked ${return_data["type"]}: ${return_data["val"]}`);
  };

  onClickLink(source, target) {
    var return_data = { type: "edge", preNode: source, nextNode: target };
    window.alert(`Clicked ${return_data["type"]}: ${return_data["preNode"]} ~ ${return_data["nextNode"]}`);
  };

  inputHandler(event) {
    this.setState({ test_input: event.target.value });
  }

  sidebar_content() {
    // side bar content func
    return (
      <div style={{ "margin-right": 20, "margin-right": 20 }}>
        <center><b>Option Menu</b></center>
        <br />
        <select id="cars">
          <option value="volvo">Volvo</option>
          <option value="saab">Saab</option>
          <option value="opel">Opel</option>
          <option value="audi">Audi</option>
        </select>
        <br />
        Input Text value: {this.state.test_input}
      </div>
    );
  }

  render() {
    return (
      <div>
        <Sidebar
          sidebar={this.sidebar_content()}
          open={this.state.sidebarOpen}
          onSetOpen={this.onSetSidebarOpen}
          styles={{ sidebar: { background: "white" }, overlay: { backgroundColor: "rgb(221, 221, 221)" } }}
        >

          <input type="text" value={this.state.test_input} onChange={this.inputHandler} />

          <Graph
            id="graph-id" // id is mandatory
            data={this.data}
            config={this.myConfig}
            // onMouseOverNode={this.onMouseOverNode}
            onClickNode={this.onClickNode}
            onClickLink={this.onClickLink}
          />
        </Sidebar>
      </div>
    )
  }
}

let styles = {
  container: {
    width: '100%',
    height: '100%',
  },
  btn_container: {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: 'auto',
    height: 'auto',
  },
  sidebar: {
    background: "white",
  },
};

export default App;
