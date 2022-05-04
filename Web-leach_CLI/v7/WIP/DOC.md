# FAILED DUE TO LACK OF KNOWLEDGE ABOUT THE ACCESSING VARIABLES

# tags:
  1. **structure**:
      {
        * `what_todo`: {
          "variable": "value",
          ....
        },
        .....
        * `exec`: [command1, command2, command3, ...]

      }
    

  2. **what_todo**:
      * `assign`: assign a value in a variable `{var: value}`
        * `var = value`
      * `append`: append a value in a variable `{var: value}`
        * `var += value`
      * `extend`: extend a list in a variable `[list]`
        * `list().extend(value)`
      * `rem_from_data`: removes a value from a variable `{var: value}`
      * `del`: delete a variable/value `[vars]`
        * `del var`
      * `exec`: execute a command `[commands]`
        * `for i in commands: exec(i)`

      * ***NOTE***:
        * `assign`, `append`, `extend`, `rem_from_data` and `del` are not
          available in the `exec` block.

  3. **value** *Special case*:
      * `[^]`:
        * `[^]` at the beginning of a value means that the value needs to be fetched from a variable. 
        * **ie:** `[^]var` will fetch the value of the variable `var`
      * `[^^][value]`:
        * `[^^][value]` at the beginning of a value means that the value needs to be fetched from a variable. 
        * **ie:** `[^^][var+var2]` will fetch the value of the variable `var+var2`
        * ⚠ will use `eval()`
        * use `[L]var` instead. make local temp variable, assign value, then use it. finally delete it.

  4. **var** *Special case*:
      * `[L]`: 
        * `[L]` at the beginning of a var name means assign a value in a local variable
        * `[L]var = value`
        * see [how to...](https://stackoverflow.com/a/8028772/11071949)



