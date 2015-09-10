class FileController < ActionController::Base

  def fileAction
    fileName = params[:fileName]
    method = params[:method]
    dataToWrite = params[:dataToWrite]

    if method == "read"
      render inline: "" # File.read("temp/" + fileName)
    else
      File.open(File.join("temp/", fileName), "w+") do |f|
        f.write(dataToWrite)
        render inline: "" # dataToWrite
      end
    end
  end
end