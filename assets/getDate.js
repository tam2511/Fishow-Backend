const getData = (days) => {
  const someDate = new Date();
  const numberOfDaysToAdd = days;
  someDate.setDate(someDate.getDate() + numberOfDaysToAdd);

  const dd = someDate.getDate();
  const mm = someDate.getMonth() + 1;
  const yy = someDate.getFullYear();
  const newmm = mm.length > 1 ? mm : '0' + mm;
  const someFormattedDate = dd + '-'+ newmm;
  return someFormattedDate;
}

const result = []

for (let i = 0; i < 10; i++) {
  result.push(getData(i))
}
console.log('result = ', result)
