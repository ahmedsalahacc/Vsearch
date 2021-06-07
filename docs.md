# Project Structure and Docs
## Project Structure
|src
--|brains
----|agent_utils.py
----|env_utils.py
----|agents.py
--|static
----|css
------|index.html
----|js
------|canvasconfig.js
--|templates
----|index.html
--|app.py
--|docs.md (crt file)


## Project Docs
### Front End
#### ./templates/index.html
#### ./css/index.css
#### ./static/canvasconfig.js
This file controls the flow of the graphical representation of the project.
##### Main Variables
const NODERADIUS = 30; ---> represents the radius of the nodes drawn by the user.

var connection = {
    connections: [],
    get_index: function(node_repr){
        for(let i=0;i<this.connections.length;i++){
            if(this.connections[i].repr === node_repr) return i;
        }
        return -1;
    }
}; ---> represents the nodes and edges in the canvas.
connections is an array of the available nodes. It keeps record of each connected nodes in the system.

var right_click_tracker = {
    events:[],
    connection: []
}; ---> represents the events clicked by the user. Used to detect which node is clicked first and which node is clicked second to keep track of the connected nodes. This variable is flushed adter two nodes are connected

let Node = {
    repr:null,
    pos:null,
    children_nodes:[],
    weights:[]
}; ---> represents each node clicked by the user. It has an array of the children nodes and the weights corresponding to each child node.

##### Main Functions
main() ---> this function is the main event loop. It gets executed  when the page loads for the first time.

draw_rect(xs,ys,xe,ye, fill_color='beige') ---> draws a rectangle starting with starting points (xs,ys) and endpoints (xe,ye) with a color of fill_color.

draw_circle(x,y,r=5,color='green') ---> draws a circle at the center (x,y) with radius 'r' and color 'color'

draw_node(e) ---> takes an event object and listens to the user clicks on the canvas (left clicks) to add a node with the corresponding alphabetical order. This function also appends the connections array in the connection object with the newly added node.

draw_edge(e) ---> takes an event object and listens to the user (right clicks) on the nodes to trigger a connection line between them. This function also updates the connection object with the added connections under each node children array.

add_weight(e) ---> takes an event object and listens to the button to add weight to the corresponding edge of appointed in the dropbox. It updates the connection object with the newly added edge.

offset(el) ---> takes an element object and returns the absolute offset of the element from the top-left corner

correct_for_canvas(e) ---> returns the position of the click with respect to the canvas (not the absolute)

get_bounds(e) ---> takes an event object and detects whether the event takes is in the region of the node or not.

### Back End
#### ./app.py
#### ./brains/env_utils.py
#### ./brains/agent_utils.py
#### ./brains/agents.py