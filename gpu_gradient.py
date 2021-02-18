import pycuda.driver as cuda
import pycuda.autoinit
import pycuda.compiler

from pycuda.compiler import SourceModule

mod = SourceModule("""#include <stdio.h>
    // __device__ float[2]  array_prefered_point_to_quit(float x, float y); // declaration
    __device__ float[2] array_prefered_point_to_quit(float x, float y)
    {
        float projection_outdoor_point[2] = {0,0};
        float unit_vector_door[2] = {1, 0};
        
        // float int_width_crowds_screen = 200;
        // float int_height_crowds_screen = 200;
        
        float MIN_DOOR_COORDINATE = 0;
        float MAX_DOOR_COORDINATE = 20;
        float int_coefficient_projection, int_not_null_coordinate;
        
        int_coefficient_projection = unit_vector_door[0] * x + unit_vector_door[1] * y;
        
        projection_outdoor_point[0] = unit_vector_door[0] * int_coefficient_projection;
        projection_outdoor_point[1] = unit_vector_door[1] * int_coefficient_projection;
       
        int_not_null_coordinate = max(projection_outdoor_point[0], projection_outdoor_point[1]);
        
        if (int_not_null_coordinate > MAX_DOOR_COORDINATE && int_not_null_coordinate > 0)
        {
            return { projection_outdoor_point[0] / int_not_null_coordinate * MAX_DOOR_COORDINATE,
            projection_outdoor_point[1] / int_not_null_coordinate * MAX_DOOR_COORDINATE};
        }
        if(MIN_DOOR_COORDINATE > int_not_null_coordinate && int_not_null_coordinate > 0):
        { 
            return {projection_outdoor_point[0]  / int_not_null_coordinate * MIN_DOOR_COORDINATE,
            projection_outdoor_point[1] / int_not_null_coordinate * MAX_DOOR_COORDINATE};
        }
        return projection_outdoor_point;
    }
    
    __global__ void gradient_vectors(float *grad, float *a, float *b, float *c)
    {
      const int i = threadIdx.x;
      // grad[i] = (b[i]) / sqrt( pow(a[i],2) + pow(b[i], 2));
      vec_coords = double[2] {a[i], b[i]};
      grad[i] = array_prefered_point_to_quit(});
    }
""")

gradient_them = mod.get_function("gradient_vectors")
