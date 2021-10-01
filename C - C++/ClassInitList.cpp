#include <iostream>
#include <string>

// Clasic init
class Entity
{
    private:
        std::string m_Name;
        int m_score;

    public:
        Entity()
        {
            m_Name = "NONE";
            m_score = 0;
        }

        Entity(const std::string& name,const int& score)
        {
            m_Name = name;
            m_score = score;
        }
};

// With Init List
class Entity"
{
    private:
        std::string m_Name;
        int m_score;

    public:
        Entity()
            : m_Name("NONE"),m_score(0)     // the orde must be the same as when they were declared
        {   
        }

        Entity(const std::string& name,const int& score)
            : m_Name(name),m_score(score)
        {
        }
};

int main()
{
    return 0;
}