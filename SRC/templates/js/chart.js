var ctx = document.getElementById("line-chart").getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: "{{labels}}",
        datasets: [{
            label: 'Insulin dose values',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: "{{values}}"
        }]
    },
    options: {
      title: {
        display: true,
        text: 'Insulin doses'
      }
    }
  });