const Stack = function () {
    this.storage = []
    this.size = 0

    // push new item to top of the stack
    this.push = function(item) {
        this.storage[this.size] = item
        this.size += 1
    }

    // pop method: removes the last item pushed in stack
    this.pop = function() {
        this.size -= 1
        const value = this.storage[this.size]
        delete this.storage[this.size]
        this.storage = this.storage.slice(0,this.size)
        return value
    }


    // peek method: returns the last element of the stack
    // without removing it from the stack
    this.peek = function() {
        if (this.size === 0) {
            return undefined
        }
        return this.storage[this.size - 1]
    }

}