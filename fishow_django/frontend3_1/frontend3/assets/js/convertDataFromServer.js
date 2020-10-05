export const convertDataFromServer = (data) => {
  if (data === null || typeof data !== 'object') {
    return null
  }
  console.log('data = ', data)
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
      const newmm = mm.length > 1 ? mm : '0' + mm
      return dd + '/' + newmm
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
  console.log('keys = ', keys)
  const newData = {}

  keys.forEach((item) => {
    if (data[item] && data[item][0] === '[' && data[item][2] !== '[') {
      // if array
      newData[item] = data[item].substr(1, data[item].length - 2).split(', ')
    } else if (data[item] && data[item][2] === '[') {
      // if phenomenon
      newData[item] = JSON.parse(data[item])
    } else {
      // if just string
      newData[item] = data[item]
    }
  })
  const length = newData.temperature_max.length
  const days = []
  const calendarDays = getData(data.date, 9)
  for (let i = 0; i < length; i++) {
    const day = {}
    keys.forEach((item) => {
      if (typeof newData[item] === 'object' && newData[item][i]) {
        day[item] = newData[item][i]
      }
    })
    days.push(day)
  }
  keys.forEach((item) => {
    if (typeof newData[item] === 'string') {
      days[item] = newData[item]
    }
    if (typeof newData[item] === 'object' && !newData[item].length) {
      days[item] = newData[item]
    }
  })
  days.forEach((day, index) => {
    day.date = calendarDays[index]
  })
  return days
}
// convertDataFromServer(datafromserver);
