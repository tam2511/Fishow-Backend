export default (object) => {
  if (object === null || object === undefined) {
    return null
  }
  const event = new Date()
  const date = {
    mouth: object.date.split('/')[1] - 1,
    day: object.date.split('/')[0],
  }
  event.setMonth(date.mouth, date.day)
  const n = event.getDay()
  const days = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']
  return days[n]
}
