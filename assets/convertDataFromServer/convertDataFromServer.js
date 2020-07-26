// const datafromserver = {
//   areal: "Московская область",
//   city: "Москва",
//   date: "2020-07-15",
//   fish: "щука",
//   gust_max: "[17, 11, 10, 9, 8, 6, 6, 9, 9]",
//   humidity_mean:
//     "[0.86125, 0.89625, 0.79, 0.7825, 0.73, 0.65875, 0.705, 0.82375, 0.775]",
//   id: 18859,
//   moon: "[0.27, 0.19, 0.12, 0.06, 0.02, 0, 0.01, 0.04, 0.1]",
//   moon_direction: "[-1, -1, -1, -1, -1, 0, 1, 1, 1]",
//   moon_text:
//     "Лунные фазы можно назвать важнейшим показателем при построении прогноза клева. Для щуки этот показатель очень важен. Фаза луны влияет на клев всегда, на прогноз нашей модели она повлияла *15 июля*, *16 июля* и *17 июля*.",
//   phenomenon:
//     "[\"['пасмурно', 'дождь']\", \"['пасмурно', 'дождь', 'гроза']\", \"['пасмурно', 'небольшой дождь']\", \"['пасмурно', 'небольшой дождь']\", \"['облачно']\", \"['ясно']\", \"['пасмурно']\", \"['малооблачно', 'небольшой дождь', 'гроза']\", \"['облачно', 'дождь', 'гроза']\"]",
//   phenomenon_warning:
//     "На данный момент для того, чтобы сказать как влияют погодные явления на клев щуки в данном регионе, нам необходимо больше данных. Для этого необходимо больше отчетов с рыбалок в этом регионе. Вы можете <strong>оставить отчет</strong> и помочь выявить закономерности нашему алгоритму более точно. ",
//   prediction_text:
//     "'Наша модель прогноза обучается и предсказывает для каждого вида рыб по-своему, в частности,\n     для щуки.Хорошо будет клевать в *ближайшие трое суток*.",
//   pressure_max: "[737, 743, 747, 749, 750, 749, 746, 745, 743]",
//   pressure_min: "[736, 736, 743, 747, 749, 747, 745, 743, 740]",
//   pressure_text:
//     "Давление является одним из самых важных показателей для определения прогноза клева щуки. ",
//   prob_max: "[0.79, 0.65, 0.63, 0.6, 0.59, 0.61, 0.62, 0.64, 0.64]",
//   prob_min: "[0.61, 0.55, 0.5, 0.56, 0.52, 0.53, 0.55, 0.55, 0.58]",
//   temperature_brief:
//     "Температура воздуха оказывает значительное влияние на клев в случае резких перепадов температуры. В случае же небольших изменений температуры воздуха клев <strong>щуки</strong> может изменится за счет других факторов. ",
//   temperature_desc:
//     '<strong>*21 июля*-*22 июля*</strong> ожидается резкое <span class="blue strong">понижение</span> температуры воздуха. <strong>*16 июля*</strong> минимальная температура воздуха будет составлять - <span class="blue strong">13</span>, а <strong>*22 июля*</strong> ожидается максимальная - <span class="red strong">25</span>. ',
//   temperature_fish:
//     'На <strong>щуку</strong> положительно влияет <span class="blue strong">понижение</span> температуры воздуха, а ее резкое <span class="red strong">повышение</span> способствует уменьшению активности рыбы. ',
//   temperature_max: "[19, 17, 19, 19, 23, 24, 22, 22, 21]",
//   temperature_mean:
//     "[17.125, 15, 16.875, 16.625, 18.125, 19.375, 19.375, 19, 18.25]",
//   temperature_min: "[15, 13, 15, 13, 13, 13, 17, 15, 14]",
//   uv_index_mean:
//     "[1.125, 0.625, 1.125, 1.125, 1.375, 1.875, 1.125, 1.375, 1.375]",
//   wind_direction: "['ЮВ', 'З', 'З', 'СЗ', 'СЗ', 'СЗ', 'СЗ', 'СЗ', 'ЮЗ']",
//   // wind_direction: "['ЮВ', 'З', 'З', 'СЗ', 'СЗ', 'СЗ', 'СЗ', 'СЗ', 'ЮЗ']",
//   wind_mean: "[2.875, 4.125, 4, 2.875, 2.625, 1.75, 1.625, 2.375, 2.125]",
//   wind_text:
//     "Направление и скорость ветра могу существенно повлиять на клев щуки. Изменения в направлении и силе воздушных потоков, по нашим прогнозам могут повлиять на клев *15 июля*.",
// };

// const convertDataFromServer = (data) => {
export const convertDataFromServer = (data) => {
  if (data === null || typeof data !== "object") {
    return null;
  }
  const getData = (fromData, days) => {
    const returnData = (a, b) => {
      const predictDate = a.split("-");
      const someDate = new Date();
      const numberOfDaysToAdd = b;
      someDate.setMonth(predictDate[1] - 1);
      someDate.setFullYear(predictDate[0]);
      someDate.setDate(Number(predictDate[2]) + numberOfDaysToAdd);
      const dd = someDate.getDate();
      const mm = someDate.getMonth() + 1;
      const newmm = mm.length > 1 ? mm : "0" + mm;
      return dd + "/" + newmm;
    };
    const result = [];
    const iterator = (numberOfDays) => {
      for (let i = 0; i < numberOfDays; i++) {
        result.push(returnData(fromData, i));
      }
    };
    iterator(days);
    return result;
  };

  const keys = Object.keys(data);
  const newData = {};

  keys.forEach((item) => {
    if (data[item][0] === '[' && data[item][2] !== '[') { // if array
      newData[item] = data[item]
          .substr(1, data[item].length - 2)
          .split(", ");
    } else if (data[item][2] === '[') { // if phenomenon
      newData[item] = JSON.parse(data[item])
    } else { // if just string
      newData[item] = data[item];
    }
  })
  const length = newData.temperature_max.length;
  const days = [];
  const calendarDays = getData(data.date, 9);
  for (let i = 0; i < length; i++) {
    const day = {};
    keys.forEach((item) => {
      if (typeof newData[item] === 'object') {
        day[item] = newData[item][i];
      }
    });
    days.push(day);
  }
  keys.forEach((item) => {
    if (typeof newData[item] === 'string') {
      days[item] = newData[item]
    }
  });
  days.forEach((day, index) => {
    day.date = calendarDays[index];
  });
  return days;
};
// convertDataFromServer(datafromserver);
