class FileController < ActionController::Base

  def fileAction
    # @tasks = Task.all
    fileName = params[:fileName]
    method = params[:method]
    dataToWrite = params[:dataToWrite]
    puts("LOGGINGGGG")
    puts(fileName)
    puts(method)
    puts(dataToWrite)

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