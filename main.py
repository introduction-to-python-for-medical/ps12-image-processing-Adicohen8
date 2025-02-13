def supress_noise(image_array):
    clean_image = median(image_array, ball(3))
    return clean_image
  
def detect_edges(clean_image):
    edgeMAG = edge_detection(clean_image)
    return edgeMAG

def convert_to_binary(edgeMAG, threshold):
    binary_image = edgeMAG > threshold
    return binary_image

def save_image(binary_image, file_path):
    edge_image = Image.fromarray(binary_image)
    edge_image.save(file_path) 

image_array = load_image('adi.jpg')
clean_image = supress_noise(image_array)
edgeMAG = detect_edges(clean_image)
threshold = 0.5
binary_image = convert_to_binary(edgeMAG, threshold)
save_image(binary_image, 'my_edges.png')

plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')
plt.show()
