## Binary Search

- In my first attempt,  I got the logic part right but used recursion to keep calling
function back
- this expiosed 2 flaws in my understanding
    1) knowing when to use recursion and when not
    2) not knowing how to ensure code I wrote is correct and works perfectly


- after watching the solution and reading [Writing correct programs](https://dl.acm.org/doi/pdf/10.1145/358476.358484) I learnt about loop invariant; which means proposing an idea before loop starts and ensuring every step of the way each line of code adheres to it
- this flow changed the approach as following:
    1) establish that n must be in range [low, high) always
    2) when its not then break
        2) I used while low < high logic, but could have also done in a for loop and break loop when low > high
    3) only adjust boundaries of low, high as I progress

