export default (days) => {
  if (days === null || days.length < 2 || typeof days === 'string') {
    return null
  }
  // console.log('days = ', typeof days)
  const whatMonth = {
    '01': 'Января',
    '02': 'Февраля',
    '03': 'Марта',
    '04': 'Апреля',
    '05': 'Мая',
    '06': 'Июня',
    '07': 'Июля',
    '08': 'Августа',
    '09': 'Сентября',
    10: 'Октября',
    11: 'Ноября',
    12: 'Декабря',
  }
  const result = []

  days.forEach((item) => {
    if (!item) return
    const arrayFromItem = item && item.split('/')
    const month =
      arrayFromItem[1].length < 2 ? '0' + arrayFromItem[1] : arrayFromItem[1]
    result.push(arrayFromItem[0] + ' ' + whatMonth[month])
  })
  return result
}
