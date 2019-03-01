# function avoidObstacles(arr) {
#     arr.sort((a,b) => a - b);
#     var correct_found = false;
#     for (var jump_size = 1; jump_size <= arr[arr.length-1]+1; jump_size++) {
#         var jump_number = 1;
#         var jump_position = jump_size*jump_number;
#         while (jump_position <= arr[arr.length-1]+jump_size) {
#             if (arr.includes(jump_position)) {
#                 break;
#             }
#             jump_number++;
#             jump_position = jump_size*jump_number;
#         }
#         if (jump_position > arr[arr.length-1]) {
#             return jump_size;
#         }
#     }
#     return false;
# }