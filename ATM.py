{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyN9UfwQZEHgfL2YTCbMvHhZ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6VVv5-_wlxTJ",
        "outputId": "2796d076-51a6-4bef-e156-921411f88cf9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "3 1 4 3 2\n",
            "[1, 3]\n",
            "[1, 3, 6]\n",
            "[1, 3, 6, 9]\n",
            "[1, 3, 6, 9, 13]\n",
            "32\n"
          ]
        }
      ],
      "source": [
        "N = int(input())\n",
        "arr = list(map(int, input().split()))\n",
        "answer = []\n",
        "arr.sort()\n",
        "\n",
        "answer.append(arr[0])\n",
        "\n",
        "for i in range(1, N):\n",
        "    answer.append(answer[-1] + arr[i])\n",
        "\n",
        "print(sum(answer))"
      ]
    }
  ]
}