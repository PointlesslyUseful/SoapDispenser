from tinymlgen import port

if __name__ == '__main__':
    tf_model = create_tf_model()
    c_code = port(tf_model)
