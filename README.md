# Project 5 Capitalist Adventure


<h1 align="center">
  <br>
    <a href="static/logo.png">
      <img src="static/logo.png" alt="Capitalist Adventure Logo" width="200">
    </a>
  <br>
</h1>

<h4 align="center"> Project 5 - Capitalist Adventure </h4>

<p align="center">
  <a href="#about-the-project">About the project</a> •
  <a href="#how-to-use">How To Use</a> •
</p>

<p align="center">
  TODO: ADD GIF
  <img src="timelapse.gif">
</p>

**List Number**: 5<br>
**Course Content**: Programação dinâmica<br>

## Students
| Matrícula  | Aluno                              |
| ---------- | ---------------------------------- |
| 15/0150792 | Victor Moura                       |
| 16/0005191 | Durval Carvalho                    |

## About the project

This project was developed for the discipline
**Algorithm Project** of FGA College in the semester 02/2019.

This project aims to analyze the stock prices of a
particular company over a given period of time and calculate
the maximum profit possible with the limited amount of buy
and sell.

The main goal was to develop an application that uses
**dynamic programming** algorithm design paradigm.

We use data provided by the [API NAME](API LINK)
to get the historical values of the stock of a particular
company.

The application when launched returns a list of companies
available for analysis.

When the company and the analysis period are determined,
the purchase and sale dates are computed which will result
in the maximum gain and is generated graphic for better
visualization.

## How To Use

  Capitalist Adventure is available in [PyPi](https://pypi.org/project/pyhuff/):

  ```sh
  $ pip install pyhuff
  ```

  ## Usage
  To shrink a file named `example.txt`:
  ```sh
  $ pyhuff example.txt
  ```

  Two files will be created:
  - **example.huff**: the encoded file
  - **example.tree.huff**: the huffman tree used to encode the file

  To restore the original file:
  ```sh
  $ pyhuff example.huff example.tree.huff decoded_example.txt
  ```
  In the example above, the decoded file will be created as `decoded_example.txt`. You can pass any filename as argument. Notice that, if the given file already exists, it will be overwritten.

  To get help, simply call:
  ```sh
  $ pyhuff
  ```
  ---

created by [Durval Carvalho](https://github.com/durvalcarvalho) and [Victor Moura](https://github.com/victorcmoura)