// let age = 18
// alert('hello')
// console.log('hello')

let person = {
    num: 18,
    uname: "xiaoze"
}
console.log(typeof (person.num))
console.log(person["uname"])

let arr = ['赵云', '马超', '关羽', '张飞', '黄忠', '刘备', '曹操']
let random = Math.floor(Math.random() * arr.length)
document.write(arr[random])
arr.splice(random, 1)
console.log(arr)

//随机颜色
function getRandomColor(flag) {
    if (flag) {
        return '#' + Math.floor(Math.random() * 0xffffff).toString(16).padStart(6, '0')
    } else {
        let r = Math.floor(Math.random() * 256)
        let g = Math.floor(Math.random() * 256)
        let b = Math.floor(Math.random() * 256)
        return 'rgb(' + r + ',' + g + ',' + b + ')'
    }
}
console.log(getRandomColor(true))

//学成在线
let data = [
    {
        src: '#',
        title: '前端开发工程师',
        num: 590
    }
]
for (let i = 0; i < data.length; i++) {
    document.write(data[i].src)
    document.write(data[i].title)
    document.write(data[i].num)
}