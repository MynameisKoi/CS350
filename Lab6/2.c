#include <stdio.h>

int main() {
    int road_length, num_areas, start, end, trees_to_move = 0;

    printf("Enter the length of the road: ");
    scanf("%d", &road_length);
    int covered_trees[road_length];

    printf("Enter how many areas are needed for new facilities: ");
    scanf("%d", &num_areas);

    for(int i = 1; i <= num_areas; i++) {
        printf("area#%d starting point & ending point: ", i);
        scanf("%d %d", &start, &end);
        for(int j = start; j <= end; j++) {
            if(!covered_trees[j]) {
                trees_to_move++;
                covered_trees[j] = 1;
            }
        }
    }

    printf("Number of trees to move: %d", trees_to_move);

    return 0;
}
