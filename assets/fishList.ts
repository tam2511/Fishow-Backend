const fishBuildList = (fishArray: Array<string>) => {
    if (fishArray && fishArray.length === 0) {
        return null;
    }
    const result: Array<object> = [];
    fishArray.forEach((fish) => {
        result.push({
            title: fish,
            image: '/fish_green/' + fish + '.jpg',
        },)
    })
    return result;
}

const fishList = [
    'щука',
    'судак',
    'окунь',
    'берш',
    'речная форель',
    'озерная форель',
    'елец',
    'чехонь',
    'сом',
    'голавль',
    'язь',
    'карп',
    'жерех',
    'лещ',
    'карась',
    'линь',
    'пескарь',
    'ротан',
    'плотва',
    'красноперка',
    'налим',
    'густера',
    'амур',
    'ерш',
    'сазан',
    'подуст',
    'толстолобик',
    'вобла',
]
// const empty:Array<null> [];

console.log('result = ', fishBuildList(fishList));