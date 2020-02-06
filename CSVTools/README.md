# Save your time while operating on CSV file!

There are some functions which will save your time while handling a CSV file.

| Function's name | Description |
| --------------- | --------------------------------------|
|[Transform](#Transform) | Turn the row into column.(The output now is text format) |

# Details

CSVOperation.Transform(ReadName, StartRow, StartColumn, SaveName = '')
  
  Turn the row into column.

  parameters:

##<T id="Transform"> Transform </T>

For example, we want to handle a CSV file named "test.csv": the area in the red box will be turned.

Code:

```
import CSVOperation

CSVOperation.Transform("test", 4, 5)

```

Here is the result:

