import pickle
  import gzip

  def compress_pickle(filepath, data):
      with gzip.open(filepath + '.gz', 'wb') as f:
          pickle.dump(data, f)

  def decompress_pickle(filepath):
      with gzip.open(filepath, 'rb') as f:
          return pickle.load(f)

  # Example usage:
  # compress_pickle('clf.pkl', your_model)
  # loaded_model = decompress_pickle('clf.pkl.gz')