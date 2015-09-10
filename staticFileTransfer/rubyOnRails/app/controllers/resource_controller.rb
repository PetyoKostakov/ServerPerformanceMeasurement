class ResourceController < ActionController::Base
  def getResource
    def concatBigString
      strArr = []
      str = ""

      for n in 1..19
        for j in 1..255
          strArr.push(j.chr.force_encoding("ISO-8859-1"))
        end
        str += strArr.join("")
      end

      return str
    end
    def generateObject
      obj = {}

      for i in 1..5
        obj["prop" + i.to_s] = concatBigString
      end

      return obj
    end


    render json: generateObject()
  end
end