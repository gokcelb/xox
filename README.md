# XOX

`XOX` is a simple tictactoe game which you can play to pass time. 

Remember how we played tictactoe on a paper when we were young? Well, `XOX` is exactly that; the only difference is that you play it on a command line interface.

Oh! I forgot, with my application, you don't write "x"s and "o"s as input, but rather "0 0" and "2 1"s. These numbers indicate the indexes of our board which is made of a 2D array.

When the application is first run, it prints out a sample input and a blank board.

```
sample input: 0 0
  |   |  
---------
  |   |  
---------
  |   |  
```

Below you can see how your input (in this case "0 1") looks on the tictactoe board.

```
> 0 1

  | x |  
---------
  |   |  
---------
  |   |  
```

Unfortunately the application is not dynamic, meaning you can only play tictactoe on a 3x board. But it is still an amusing pass-time activity!