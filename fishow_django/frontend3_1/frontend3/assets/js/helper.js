export default (day) => {
  if (day && day.date) {
    const months = {
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

    return day.date.split('/')[0] + ' ' + months[day.date.split('/')[1]]
  } else {
    return null
  }
}
