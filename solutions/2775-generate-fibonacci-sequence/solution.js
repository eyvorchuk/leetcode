/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    yield 0;
    yield 1;
    let val = 1;
    let prev = 0;
    while (true) {
        let next = val + prev;
        prev = val;
        val = next;
        yield val;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
