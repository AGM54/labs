vertex_shader = '''
#version 450 core

layout (location = 0 ) in vec3 position;
layout (location = 1 ) in vec2 texCoords;
layout (location = 2 ) in vec3 normals;



uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;


out vec2 UVs;
out vec3 outNormals;

void main()
{
    vec4 newPos = vec4(position.x, position.y, position.z, 1);
    
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * newPos;
    UVs = texCoords;
    outNormals = (modelMatrix * vec4(normals, 0.0)).xyz;


}


'''

fragmet_shader = '''
#version 450 core

layout (binding  = 0) uniform sampler2D tex;

uniform vec3 dirLight;

in vec2 UVs;
in vec3 outNormals;

out vec4 fragColor;

void main()
{
    float intensity = dot(outNormals, -dirLight);    
    fragColor = texture(tex, UVs) * max(0, (min(1,intensity)));
}
'''





fragmet_shader1 = '''
#version 450 core

uniform sampler2D particleTexture;
uniform vec3 glowColor; // Color de la fosforescencia
uniform float glowIntensity; // Intensidad del brillo

in vec2 UVs;

out vec4 fragColor;

void main()
{
    vec4 texColor = texture(particleTexture, UVs);


    vec3 glow = glowColor * glowIntensity;


    fragColor = vec4(texColor.rgb + glow, texColor.a);
}



'''


vertex_shader1 = '''

#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 outNormals;

void main()
{
    // Transformación de la posición
    vec3 transformedPosition = position;
    
    // Por ejemplo, aplicamos una deformación sencilla basada en el tiempo
    transformedPosition.x += sin(time + position.x);
    transformedPosition.y += cos(time + position.y);

    vec4 newPos = vec4(transformedPosition, 1.0);
    
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * newPos;
    UVs = texCoords;
    outNormals = (modelMatrix * vec4(normals, 0.0)).xyz;
}


'''