/* eslint-disable */
export const convertDataFromServer = (data) => {
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
  const keys = Object.keys(data)
  const length = data.temperature_max.length
  const days = []
  const calendarDays = getData(data.date, 9)
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
