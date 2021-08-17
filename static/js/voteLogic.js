//Sets up data array
let data = [
    {name: "Eric S.", votes:0},
    {name: "Sally J.", votes:0},
    {name: "Jesse H.", votes:0}
];


//Creates a custom alert with the name of person who is voted for by the user
function onVote(){

    //Grabs the three radio buttons from poll.html page
    let choices = document.getElementsByClassName("vote");
    let votedFor = "";

    //Loops through radio buttons to find which one (if any) is checked
    for(let i = 0; i < choices.length; i++){
        if (choices[i].checked === true){
            votedFor = choices[i].value;
        }
    }

    //Creates custom alert message, assuming submission is valid
    if(votedFor !== ""){
        updateVotes(votedFor);
    }


}

window.onload = function(){
    getVotes();
};

//Function saves votes for each candidate to local storage
function getVotes(){
    let firstVotes;
    let secondVotes;
    let thirdVotes;
    let nomineeOne = document.getElementById("nomineeOne");
    let nomineeTwo = document.getElementById("nomineeTwo");
    let nomineeThree = document.getElementById("nomineeThree");

    //If there has been no local storage created
    if(localStorage.getItem("firstVotes") == null){
        localStorage.setItem("firstVotes", "0");
        localStorage.setItem("secondVotes", "0");
        localStorage.setItem("thirdVotes", "0");

        firstVotes = localStorage.getItem("firstVotes");
        secondVotes = localStorage.getItem("secondVotes");
        thirdVotes = localStorage.getItem("thirdVotes");

        nomineeOne.textContent = "Current Vote Count:  " + firstVotes;
        nomineeTwo.textContent = "Current Vote Count:  " + secondVotes;
        nomineeThree.textContent = "Current Vote Count:  " + thirdVotes;
    }

    else{
        firstVotes = localStorage.getItem("firstVotes");
        secondVotes = localStorage.getItem("secondVotes");
        thirdVotes = localStorage.getItem("thirdVotes");

        nomineeOne.textContent = "Current Vote Count:  " + firstVotes;
        nomineeTwo.textContent = "Current Vote Count: " + secondVotes;
        nomineeThree.textContent = "Current Vote Count:  " + thirdVotes;

        data = [
            {name: "Eric S.", votes:localStorage.getItem("firstVotes")},
            {name: "Sally J.", votes:localStorage.getItem("secondVotes")},
            {name: "Jesse H.", votes:localStorage.getItem("thirdVotes")}

        ]
    }

    //This establishes dimensions for svg
    const width = screen.width;
    const height = screen.height / 2;
    const margin = { top: 50, bottom: 50, left: 50, right: 50 };

    //Creates svg and sets dimensions
    let svg = d3.select('#d3-container')
        .append('svg')
        .attr('width', width - margin.left - margin.right)
        .attr('height', height - margin.top - margin.bottom)
        .attr("viewBox", [0, 0, width, height]);

    //Sets domain for x axis
    const x = d3.scaleBand()
        .domain(d3.range(data.length))
        .range([margin.left, width - margin.right])
        .padding(0.1)

    //Sets range for y axis
    const y = d3.scaleLinear()
        .domain([0, 10])
        .range([height - margin.bottom, margin.top])

    //Appends rectangles to svg and filters them by data
    svg
        .append("g")
        .attr("fill", 'royalblue')
        .selectAll("rect")
        .data(data.sort((a, b) => d3.descending(a.votes, b.votes)))
        .join("rect")
        .attr("x", (d, i) => x(i))
        .attr("y", d => y(d.votes))
        .attr('title', (d) => d.votes)
        .attr("class", "rect")
        .attr("height", d => y(0) - y(d.votes))
        .attr("width", x.bandwidth());

    //Sets y axis parameters
    function yAxis(g) {
        g.attr("transform", `translate(${margin.left}, 0)`)
            .call(d3.axisLeft(y).ticks(null, data.format))
            .attr("font-size", '30px')
    }

    //Sets x axis parameters
    function xAxis(g) {
        g.attr("transform", `translate(0,${height - margin.bottom})`)
            .call(d3.axisBottom(x).tickFormat(i => data[i].name))
            .attr("font-size", '30px')
    }

    //Appends svg and writes to screen
    svg.append("g").call(xAxis);
    svg.append("g").call(yAxis);
    svg.node();


}

//This function updates the vote totals and chart
function updateVotes(votedFor){
    let winner = false;
    let winnerName = "";
    if(document.getElementById("Eric").checked === true){
        let currVotes = parseInt(localStorage.getItem("firstVotes"));
        localStorage.setItem("firstVotes", (currVotes + 1).toString());
        if(currVotes >= 10){
            winner = true;
            winnerName = "Eric S.";
        }
        let nomineeOne = document.getElementById("nomineeOne");
        nomineeOne.textContent = "Current Vote Count: " + localStorage.getItem("firstVotes");
    }

    else if(document.getElementById("Sally").checked === true){
        let currVotes = parseInt(localStorage.getItem("secondVotes"));
        localStorage.setItem("secondVotes", (currVotes + 1).toString());
        if(currVotes >= 10){
            winner = true;
            winnerName = "Sally J.";
        }
        let nomineeTwo = document.getElementById("nomineeTwo");
        nomineeTwo.textContent = "Current Vote Count: " + localStorage.getItem("secondVotes");
    }

    else {
        let currVotes = parseInt(localStorage.getItem("thirdVotes"));
        localStorage.setItem("thirdVotes", (currVotes + 1).toString());
        if(currVotes >= 10){
            winner = true;
            winnerName = "Jesse H.";
        }
        let nomineeThree = document.getElementById("nomineeThree");
        nomineeThree.textContent = "Current Vote Count: " + localStorage.getItem("thirdVotes");

    }

    data = [
        {name: "Eric S.", votes:localStorage.getItem("firstVotes")},
        {name: "Sally J.", votes:localStorage.getItem("secondVotes")},
        {name: "Jesse H.", votes:localStorage.getItem("thirdVotes")}

    ]

    if(winner === false){
        alert("Thank you for voting for: " + votedFor);
        updateChart();
    }
    else{
        alert(winnerName + " has already won!");
    }


}

//Updates chart data
function updateChart(){
    const width = screen.width;
    const height = screen.height / 2;
    const margin = { top: 50, bottom: 50, left: 50, right: 50 };

    const x = d3.scaleBand()
        .domain(d3.range(data.length))
        .range([margin.left, width - margin.right])
        .padding(0.1)

    const y = d3.scaleLinear()
        .domain([0, 10])
        .range([height - margin.bottom, margin.top])

    let svg = d3.select("#d3-container");

    svg
        .selectAll("rect")
        .data(data.sort((a, b) => d3.descending(a.votes, b.votes)))
        .attr("x", (d, i) => x(i))
        .attr("y", d => y(d.votes))
        .attr('title', (d) => d.votes)
        .attr("class", "rect")
        .attr("height", d => y(0) - y(d.votes))
        .attr("width", x.bandwidth());
}
