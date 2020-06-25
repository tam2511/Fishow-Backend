export const convertDataFromServer = (data) => {
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
  const newData = {}

  const excludeKeys = {
    id: 'id',
    date: 'date',
    areal: 'areal',
    city: 'city',
    fish: 'fish',
    id_array: 'id_array',
    wind_direction: 'wind_direction',
  }

  keys.forEach((item) => {
    if (!excludeKeys[item]) {
      try {
        newData[item] = JSON.parse(data[item])
      } catch (e) {
        newData[item] = data[item]
      }
    } else {
      newData[item] = data[item]
    }
  })

  // transform wind_direction to array
  newData.wind_direction = newData.wind_direction
    .substr(1, newData.wind_direction.length - 2)
    .split(', ')

  const excludeKeysNew = {
    id: 'id',
    date: 'date',
    areal: 'areal',
    city: 'city',
    fish: 'fish',
    id_array: 'id_array',
  }

  const length = newData.temperature_max.length

  const days = []
  const calendarDays = getData(data.date, 9)

  for (let i = 0; i < length; i++) {
    const day = {}
    keys.forEach((item) => {
      if (!excludeKeysNew[item]) {
        day[item] = newData[item][i]
      } else {
        day[item] = newData[item]
      }
    })
    days.push(day)
  }
  days.forEach((day, index) => {
    day.date = calendarDays[index]
  })

  return days
}
