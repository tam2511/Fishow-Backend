export default (fromData, days) => {
  const returnData = (a, b) => {
    if (!a || !b) return null
    console.log(a)
    const predictDate = a.split('-')
    const someDate = new Date()
    const numberOfDaysToAdd = b
    someDate.setMonth(predictDate[1] - 1)
    someDate.setFullYear(predictDate[0])
    someDate.setDate(Number(predictDate[2]) + numberOfDaysToAdd)
    const dd = someDate.getDate()
    const mm = someDate.getMonth() + 1
    const newmm = mm.length > 1 ? mm : mm
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
