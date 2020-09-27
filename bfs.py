{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def bfs(G, s):\n",
    "    n = len(G)\n",
    "    path = [None]*n\n",
    "    visited = [False]*n\n",
    "    queue = [s]\n",
    "    visited[s] = True\n",
    "    while len(queue) > 0:\n",
    "        u = queue[0]\n",
    "        queue = queue[1:]\n",
    "        #print(G[u])\n",
    "        for v in G[u]:\n",
    "            if not visited[v]:\n",
    "                queue.append(v)\n",
    "                path[v] = u\n",
    "                visited[v] = True\n",
    "    return path"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
