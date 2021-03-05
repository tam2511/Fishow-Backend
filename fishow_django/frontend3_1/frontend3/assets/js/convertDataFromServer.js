/* eslint-disable */
export const convertDataFromServer = (data, type = null) => {
  if (data === null || typeof data !== 'object') {
    return null
  }
  const getData = (fromData, days) => {
    const returnData = (a, b) => {
      const predictDate = a.split('-')
      const someDate = new Date()
      const numberOfDaysToAdd = b
      someDate.setMonth(predictDate[1] - 1)
      someDate.setFullYear(predictDate[0])
      someDate.setDate(Number(predictDate[2]) + numberOfDaysToAdd)
      const dd = someDate.getDate()
      const mm = someDate.getMonth() + 1
      return dd + '/' + mm
    }
    const result = []
    const iterator = (numberOfDays) => {
      for (let i = 0; i < numberOfDays; i++) {
        result.push(returnData(fromData, i))
      }
    }
    iterator(days)
    return result
  }
  // console.log('data = ', data);
  const keys = Object.keys(data)
  // console.log(keys);
  const length = data.temperature_max ? data.temperature_max.length : data.temperature.length
  const days = []
  const time = ['0:00', '3:00', '6:00', '9:00', '12:00', '15:00', '18:00', '21:00'];
  const calendarDays = type ? time : getData(data.date, 9);
  // console.log('calendarDays = ', calendarDays);
  for (let i = 0; i < length; i++) {
    const day = {}
    keys.forEach((item) => {
      if (typeof data[item] === 'object') {
        day[item] = data[item][i]
      }
    })
    days.push(day)
  }
  keys.forEach((item) => {
    if (typeof data[item] === 'string') {
      days[item] = data[item]
    }
    if (typeof data[item] === 'object' && !data[item].length) {
      days[item] = data[item]
    }
  })
  days.forEach((day, index) => {
    day.date = calendarDays[index]
  })

  // return null
  return days
}
// convertDataFromServer(datafromserver);
