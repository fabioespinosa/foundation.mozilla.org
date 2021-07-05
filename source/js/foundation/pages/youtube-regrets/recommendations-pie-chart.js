import { Chart, registerables } from 'chart.js';

export const initYouTubeRegretsRecommendationsPieChart = () => {
  Chart.register(...registerables);

  const categoriesChart = document.getElementById('recommendations-pie-chart');
  const ctx = categoriesChart.getContext('2d');
  const labelFormat = gettext("%s%");

  const chart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: [
        gettext('Recommendation'),
        gettext('Search'),
        gettext('Other')
      ],
      datasets: [{
        data: [71.1, 21.5, 7.47],
        backgroundColor: [
          '#FC4147',
          '#080708',
          '#FBD5D7',
        ],
      }]
    },
    options: {
      locale: 'fr',
      plugins: {
        legend: {
          labels: {
            font: {
              size: 18,
              family: 'Nunito Sans',
              color: 'black',
            },
          }
        },
        tooltip: {
          callbacks: {
            label: (context) => interpolate(labelFormat, [context.parsed]),
          },
        },
      },
    }
  });
}
