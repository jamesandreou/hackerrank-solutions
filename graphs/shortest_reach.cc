// Written by James Andreou, University of Waterloo
// Hackerrank.com BFS Shortest Reach

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

// Adjacency List to store graph.
typedef vector <vector <int> > GRAPH;

void findShortestReach(GRAPH g, int start){
  int distance [g.size()];
  for(int i = 0; i < g.size(); i++){
    distance[i] = -1;
  }
  distance[start] = 0;

  // BFS and update distance at each breadth iteration
  queue <int> nodeQueue;
  nodeQueue.push(start);
  while(!nodeQueue.empty()){
    int curNode = nodeQueue.front();
    nodeQueue.pop();
    for(int i = 0; i < g[curNode].size(); i++){
      int edgeTail =  g[curNode][i];
      if(distance[edgeTail] == -1){
        nodeQueue.push(edgeTail);
        distance[edgeTail] = distance[curNode] + 6;
      }
    }
  }
  for(int i = 0; i < g.size(); i++){
    if(i != start) cout << distance[i] << " ";
  }
  cout << endl;
}

int main() {
    GRAPH g;
    // Read input and call BFS function for each test
    int nTests, n, m, n1, n2, start;
    cin >> nTests;
    for(int i = 0; i < nTests; i++){
      cin >> n >> m;
      // Init all nodes
      for(int j = 0; j < n; j++){
        g.push_back(vector<int>());
      }
      // Init edges
      for(int j = 0; j < m; j++){
        cin >> n1 >> n2;
        g[n1-1].push_back(n2-1);
        g[n2-1].push_back(n1-1);
      }
      cin >> start;
      findShortestReach(g, start-1);
      // Clear graph
      for(int j = 0; j < g.size(); j++){
        g[j].clear();
      }
      g.clear();
    }
    return 0;
}
