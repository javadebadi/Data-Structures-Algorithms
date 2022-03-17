let stack = new Stack()

console.log(stack.size)

let count = 0


const pushBtn = document.getElementById("push-btn")
const popBtn = document.getElementById("pop-btn")
const peekBtn = document.getElementById("peek-btn")
const stackLength = document.getElementById("stack-length")
const stackItems = document.getElementById("stack-items")
pushBtn.addEventListener('click', handlePushBtnClick)
popBtn.addEventListener('click', handlePopBtnClick)
peekBtn.addEventListener('click', handlePeekBtnClick)


function display () {
    stackLength.innerText = stack.size
    
    stackItems.innerHTML = ""
    for (let item of stack.storage) {
        const div = document.createElement('div')
        div.setAttribute('class', 'stack-box')
        div.innerText = item
        console.log(div)
        stackItems.prepend(div)
    }
}

function handlePushBtnClick() {
    count = stack.size + 1
    stack.push(`ITEM #${count}`)
    display()
}

function handlePopBtnClick() {
    if (count === 0) {
        return undefined
    }
    count = stack.size - 1
    stack.pop()
    display()
}

function handlePeekBtnClick() {
    window.alert(`Peeked Item = ${stack.peek()}`)
    display()
}